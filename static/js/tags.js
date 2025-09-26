document.addEventListener('DOMContentLoaded', function() {
                            const selectedTagsContainer = document.getElementById('selected-tags');
                            const availableTagsContainer = document.getElementById('available-tags');
                            const noTagsMessage = document.getElementById('no-tags-message');
                            const newTagInput = document.getElementById('new-tag-input');
                            const addNewTagBtn = document.getElementById('add-new-tag-btn');
                            const skillsSelect = document.getElementById('id_skills');
                            const newSkillsInput = document.getElementById('id_new_skills');
                            
                            let selectedSkills = new Set();
                            let newSkills = new Set();
                            
                            // Initialize with pre-selected skills from form
                            if (skillsSelect) {
                                Array.from(skillsSelect.selectedOptions).forEach(option => {
                                    selectedSkills.add(option.value);
                                    addSelectedTag(option.value, option.text, false);
                                });
                            }
                            
                            // Initialize with new skills from form (for edit mode)
                            if (newSkillsInput && newSkillsInput.value) {
                                const existingNewSkills = newSkillsInput.value.split(',').map(s => s.trim()).filter(s => s);
                                existingNewSkills.forEach(skillName => {
                                    const tagId = 'new_' + skillName.replace(/\s+/g, '_');
                                    newSkills.add(skillName);
                                    addSelectedTag(tagId, skillName, true);
                                });
                            }
                            
                            // Style available tag buttons
                            function styleTagButtons() {
                                document.querySelectorAll('.tag-button').forEach(button => {
                                    const skillId = button.dataset.skillId;
                                    if (selectedSkills.has(skillId)) {
                                        button.className = 'tag-button px-3 py-1 text-sm font-medium rounded-full border-2 border-[#D4AF37] bg-[#D4AF37] text-black transition-all duration-200 opacity-50 cursor-not-allowed';
                                        button.disabled = true;
                                    } else {
                                        button.className = 'tag-button px-3 py-1 text-sm font-medium rounded-full border border-gray-300 bg-white text-gray-700 hover:border-[#D4AF37] hover:bg-[#D4AF37] hover:text-black transition-all duration-200 cursor-pointer';
                                        button.disabled = false;
                                    }
                                });
                            }
                            
                            // Add selected tag to display
                            function addSelectedTag(skillId, skillName, isNew = false) {
                                // Hide no tags message
                                if (noTagsMessage && noTagsMessage.style.display !== 'none') {
                                    noTagsMessage.style.display = 'none';
                                }
                                
                                const tagElement = document.createElement('span');
                                tagElement.className = 'inline-flex items-center px-3 py-1 text-sm font-medium rounded-full bg-[#D4AF37] text-black border border-[#D4AF37] shadow-sm';
                                tagElement.innerHTML = `
                                    <span class="mr-2">${skillName}</span>
                                    <button type="button" class="text-black hover:text-red-600 transition-colors duration-200 focus:outline-none" onclick="removeTag('${skillId}', ${isNew})">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                                        </svg>
                                    </button>
                                `;
                                tagElement.dataset.skillId = skillId;
                                tagElement.dataset.isNew = isNew;
                                tagElement.dataset.skillName = skillName;
                                selectedTagsContainer.appendChild(tagElement);
                            }
                            
                            // Remove tag function (global scope for onclick)
                            window.removeTag = function(skillId, isNew) {
                                const tagElement = selectedTagsContainer.querySelector(`[data-skill-id="${skillId}"]`);
                                if (!tagElement) return;
                                
                                const skillName = tagElement.dataset.skillName;
                                
                                if (isNew) {
                                    newSkills.delete(skillName);
                                } else {
                                    selectedSkills.delete(skillId);
                                }
                                
                                // Remove visual tag
                                tagElement.remove();
                                
                                // Show "no tags" message if no tags selected
                                const remainingTags = selectedTagsContainer.querySelectorAll('[data-skill-id]');
                                if (remainingTags.length === 0) {
                                    noTagsMessage.style.display = 'block';
                                }
                                
                                styleTagButtons();
                                updateFormFields();
                            };
                            
                            // Update hidden form fields
                            function updateFormFields() {
                                if (skillsSelect) {
                                    // Clear all selections first
                                    Array.from(skillsSelect.options).forEach(option => {
                                        option.selected = selectedSkills.has(option.value);
                                    });
                                }
                                
                                if (newSkillsInput) {
                                    newSkillsInput.value = Array.from(newSkills).join(', ');
                                }
                            }
                            
                            // Handle available tag clicks
                            availableTagsContainer.addEventListener('click', function(e) {
                                if (e.target.classList.contains('tag-button') && !e.target.disabled) {
                                    const skillId = e.target.dataset.skillId;
                                    const skillName = e.target.dataset.skillName;
                                    
                                    selectedSkills.add(skillId);
                                    addSelectedTag(skillId, skillName, false);
                                    styleTagButtons();
                                    updateFormFields();
                                }
                            });
                            
                            // Handle new tag addition
                            function addNewTag() {
                                const newTagName = newTagInput.value.trim();
                                if (newTagName && !Array.from(newSkills).includes(newTagName)) {
                                    const tagId = 'new_' + newTagName.replace(/\s+/g, '_');
                                    newSkills.add(newTagName);
                                    addSelectedTag(tagId, newTagName, true);
                                    newTagInput.value = '';
                                    updateFormFields();
                                }
                            }
                            
                            addNewTagBtn.addEventListener('click', addNewTag);
                            
                            // Handle Enter key in new tag input
                            newTagInput.addEventListener('keypress', function(e) {
                                if (e.key === 'Enter') {
                                    e.preventDefault();
                                    addNewTag();
                                }
                            });
                            
                            // Initial setup
                            styleTagButtons();
                            updateFormFields();
                            
                            // Show/hide no tags message based on initial state
                            const initialTags = selectedTagsContainer.querySelectorAll('[data-skill-id]');
                            if (initialTags.length > 0) {
                                noTagsMessage.style.display = 'none';
                            }
                        });