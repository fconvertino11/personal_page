document.addEventListener('DOMContentLoaded', function () {
    const soundButton = document.getElementById('soundButton');

    // You can replace 'path/to/your/sound.mp3' with the actual path to your sound file
    const sound = new Audio('path/to/your/sound.mp3');

    soundButton.addEventListener('click', function () {
        sound.play();
    });
});
