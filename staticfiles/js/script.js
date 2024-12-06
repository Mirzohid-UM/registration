document.addEventListener("DOMContentLoaded", function () {
    const sections = document.querySelectorAll(".form-section");
    const backBtn = document.querySelector('.btn-back');
    const nextBtn = document.querySelector('.btn-next');
    let currentSectionIndex = 0;

    function showSection(index) {
        sections.forEach((section, i) => {
            section.classList.toggle("active", i === index);
        });

        backBtn.style.visibility = index === 0 ? 'hidden' : 'visible';
        nextBtn.textContent = index === sections.length - 1 ? 'Submit' : 'Next';

        nextBtn.onclick = index === sections.length - 1
            ? () => document.getElementById("registrationForm").submit()
            : () => { currentSectionIndex++; showSection(currentSectionIndex); };
    }

    backBtn.addEventListener("click", () => {
        if (currentSectionIndex > 0) {
            currentSectionIndex--;
            showSection(currentSectionIndex);
        }
    });

    showSection(currentSectionIndex);
});
