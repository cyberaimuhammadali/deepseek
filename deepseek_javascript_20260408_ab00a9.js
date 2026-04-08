const tg = window.Telegram.WebApp;
tg.expand();
tg.MainButton.setText("Bron qilish");
tg.MainButton.hide();

let selectedService = null;

async function loadServices() {
    const res = await fetch('https://your-backend.onrender.com/api/services');
    const services = await res.json();
    const container = document.getElementById('service-list');
    container.innerHTML = '';
    services.forEach(s => {
        const card = document.createElement('div');
        card.className = 'service-card';
        card.innerHTML = `<span>${s.name_uz}</span><span>${s.price} so'm</span>`;
        card.onclick = () => {
            selectedService = s;
            document.getElementById('booking-form').style.display = 'block';
            loadMasters(s.id);
        };
        container.appendChild(card);
    });
}

async function loadMasters(serviceId) {
    const res = await fetch(`https://your-backend.onrender.com/api/masters?service_id=${serviceId}`);
    const masters = await res.json();
    const select = document.getElementById('master-select');
    select.innerHTML = masters.map(m => `<option value="${m.id}">${m.name}</option>`).join('');
}

document.getElementById('confirm-booking').onclick = async () => {
    const masterId = document.getElementById('master-select').value;
    const datetime = document.getElementById('datetime').value;
    const res = await fetch('https://your-backend.onrender.com/api/book', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            user_id: tg.initDataUnsafe.user.id,
            service_id: selectedService.id,
            master_id: masterId,
            booking_time: datetime
        })
    });
    if (res.ok) {
        tg.showAlert("Bron muvaffaqiyatli! Tez orada siz bilan bog'lanamiz.");
        tg.close();
    } else {
        tg.showAlert("Xatolik, qaytadan urinib ko'ring.");
    }
};

loadServices();