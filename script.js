// Add event listener to the consent form submission
document.getElementById('consentForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const consentCheckbox = document.getElementById('consent');
    if (!consentCheckbox.checked) {
        alert('Please consent to participate in the study.');
        return;
    }

    // Redirect to survey.html
    window.location.href = 'survey.html';
});
