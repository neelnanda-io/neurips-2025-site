// Color coding for schedule table
document.addEventListener('DOMContentLoaded', function() {
    // Only run on schedule page
    if (!document.querySelector('.schedule-page')) return;
    
    // Get all table rows (skip header)
    const rows = document.querySelectorAll('.schedule-page table tr');
    
    rows.forEach(row => {
        const activityCell = row.cells[1]; // Second column contains activity
        if (!activityCell) return;
        
        const activity = activityCell.textContent.toLowerCase();
        
        // Apply classes based on activity type
        if (activity.includes('contributed talks')) {
            row.classList.add('contributed-talks');
        } else if (activity.includes('invited talk') || activity.includes('survey talk')) {
            row.classList.add('invited-talk');
        } else if (activity.includes('poster session')) {
            row.classList.add('poster-session');
        } else if (activity.includes('panel')) {
            row.classList.add('panel-discussion');
        } else {
            // Everything else (breaks, lunch, social, etc.)
            row.classList.add('other-activity');
        }
    });
});