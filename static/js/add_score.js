document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('add-score-form');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', function (event) {
        // Xatolarni tozalash
        errorMessage.classList.add('d-none');
        errorMessage.textContent = '';

        // Xatolarni yig'ish
        const errors = [];
        const citizenship = document.getElementById('citizenship').value.trim();
        const educationLevel = document.getElementById('educationLevel').value.trim();

        if (!citizenship) {
            errors.push('Fuqarolikni kiriting.');
        }

        if (!educationLevel) {
            errors.push('Ta\'lim darajasini tanlang.');
        }

        if (educationLevel === 'Oliy ta\'lim') {
            const university = document.getElementById('university').value.trim();
            const courseYear = document.getElementById('course_year').value.trim();

            if (!university) {
                errors.push('Oliy ta\'lim uchun universitet nomini kiriting.');
            }

            if (!courseYear) {
                errors.push('Oliy ta\'lim uchun kurs yilini kiriting.');
            }
        } else if (educationLevel === 'O\'rta ta\'lim') {
            const schoolName = document.getElementById('school_name').value.trim();

            if (!schoolName) {
                errors.push('O\'rta ta\'lim uchun maktab nomini kiriting.');
            }
        }

        // Agar xatolar mavjud bo'lsa, ularni foydalanuvchiga ko'rsatish
        if (errors.length > 0) {
            event.preventDefault(); // Formani yuborishni to'xtatish
            errorMessage.textContent = errors.join(' ');
            errorMessage.classList.remove('d-none');
        }
    });
});
