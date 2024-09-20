document.addEventListener('DOMContentLoaded', function() {
    // Get all section headers (folders)
    const sections = document.querySelectorAll('.toc-section');

    sections.forEach(section => {
        // Initially collapse all sections
        const nestedList = section.nextElementSibling;
        nestedList.style.display = 'none';  // Hide nested items

        // Add a click event listener to each section header
        section.addEventListener('click', function() {
            const isExpanded = nestedList.style.display === 'block';
            nestedList.style.display = isExpanded ? 'none' : 'block';

            // Toggle the icon or class if you want to indicate the collapse/expand
            section.classList.toggle('expanded', !isExpanded);
        });
    });
});
