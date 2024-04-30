console.log('Hello, world!');

document.addEventListener('DOMContentLoaded', function () {
    const thumbnails = document.querySelectorAll('.thumbnail');

    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function () {
            const imageUrl = this.getAttribute('src');
            const modalContent = `
                <div class="modal-content">
                    <span class="close-button">&times;</span>
                    <img src="${imageUrl}" style="max-width: 100%; max-height: 100vh;">
                </div>
            `;

            showModal('Image Preview', modalContent);
        });
    });

    function showModal(title, content) {
        const modal = document.createElement('div');
        modal.classList.add('modal');

        modal.innerHTML = content;
        document.body.appendChild(modal);

        const closeButton = modal.querySelector('.close-button');
        closeButton.addEventListener('click', function () {
            modal.remove();
        });
    }
});
