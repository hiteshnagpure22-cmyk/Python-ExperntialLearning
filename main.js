// Contacts List Management System - JavaScript Utilities
// S. B. Jain Institute of Technology, Management & Research, Nagpur
// Author: Hitesh Nagpure (USN: CD25085)

document.addEventListener('DOMContentLoaded', () => {
    // Auto dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            setTimeout(() => alert.remove(), 400);
        }, 5000);
    });

    // Keyboard shortcuts (e.g. Esc to close modals)
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            const deleteModal = document.getElementById('deleteModal');
            if (deleteModal && deleteModal.style.display !== 'none') {
                deleteModal.style.display = 'none';
            }
        }
    });
});
