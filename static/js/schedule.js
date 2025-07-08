// Color coding for schedule table
document.addEventListener('DOMContentLoaded', function() {
    // Function to process schedule tables
    function processScheduleTable(table) {
        const rows = table.querySelectorAll('tr');
        
        rows.forEach(row => {
            const activityCell = row.cells[1]; // Second column contains activity
            if (!activityCell) return;
            
            const activityText = activityCell.textContent;
            const activity = activityText.toLowerCase();
            
            // Bold speaker names in "Talk:" entries
            if (activity.startsWith('talk:')) {
                // Extract speaker name after "Talk:" and bold it
                const html = activityCell.innerHTML;
                const boldedHtml = html.replace(/Talk:\s*(.+)/, 'Talk: <strong>$1</strong>');
                activityCell.innerHTML = boldedHtml;
            }
            
            // Apply classes based on activity type
            if (activity.includes('contributed talks')) {
                row.classList.add('contributed-talks');
            } else if (activity.includes('talk:') || activity.includes('survey talk')) {
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
    }
    
    // Process tables on schedule page
    const scheduleTables = document.querySelectorAll('.schedule-page table');
    scheduleTables.forEach(processScheduleTable);
    
    // Also process embedded schedule tables
    const embeddedTables = document.querySelectorAll('.embedded-schedule table');
    embeddedTables.forEach(processScheduleTable);
});