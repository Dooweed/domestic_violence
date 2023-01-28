let audioStream, videoStream,
    audioRecorder, videoRecorder,
    audioChunks, videoChunks,
    counter = 1,
    log = console.log.bind(console);

const videoConfig = {
        tag: 'video',
        type: 'video/webm',
        ext: '.mp4',
        gUM: {video: true, audio: true}
    },
    audioConfig = {
        tag: 'audio',
        type: 'audio/ogg',
        ext: '.ogg',
        gUM: {audio: true}
    };

function initializeAudio() {
    navigator.mediaDevices.getUserMedia(audioConfig.gUM).then(_stream => {
        audioStream = _stream;
        audioRecorder = new MediaRecorder(audioStream);
        audioRecorder.ondataavailable = e => {
            audioChunks.push(e.data);
            if (audioRecorder.state === 'inactive')
                makeLink(audioChunks, audioConfig);
        };
        log('got audio successfully');
    }).catch(log);
}

initializeAudio();

function initializeVideo() {
    navigator.mediaDevices.getUserMedia(videoConfig.gUM).then(_stream => {
        videoStream = _stream;
        videoRecorder = new MediaRecorder(videoStream);
        videoRecorder.ondataavailable = e => {
            videoChunks.push(e.data);
            if (videoRecorder.state === 'inactive')
                makeLink(videoChunks, videoConfig);
        };
        log('got video successfully');
    }).catch(log);
}

initializeVideo();
navigator.geolocation.getCurrentPosition((position) => {
    console.log('Successfully accessed geoposition', position)
});

const sosInitBtn = document.getElementById('sosInitBtn'),
    sosSaveBtn = document.getElementById('sosSaveBtn'),
    nameTag = document.getElementById('name'),
    phoneTag = document.getElementById('phone'),
    address = 'Ул. Кары-Ниязи 17а подъезд 2 квартира 33';

sosInitBtn.onclick = e => {
    let url = sosInitBtn.getAttribute('data-url') + `?address=${address}&name=${nameTag.innerText}&phone=${phoneTag.innerText}`;

    navigator.geolocation.getCurrentPosition((position) => {
        url += `&latitude=${position.coords.latitude}&longitude=${position.coords.longitude}`;
        console.log('Sending SOS request')
        fetch(url, {
           headers: {
              'Accept': 'application/json'
           }})
        .then(response => response.text())
        .then(text => console.log(text))
    })

    sosInitBtn.parentElement.classList.add('active');
    audioChunks = [];
    videoChunks = [];
    audioRecorder.start();
    videoRecorder.start();
}


sosSaveBtn.onclick = e => {
    sosInitBtn.parentElement.classList.remove('active');
    audioRecorder.stop();
    videoRecorder.stop();
    counter++;
}


function makeLink(chunks, mediaConfig) {
    let blob = new Blob(chunks, {type: mediaConfig.type}),
        url = URL.createObjectURL(blob),
        li = document.createElement('li'),
        mt = document.createElement(mediaConfig.tag),
        hf = document.createElement('a');
    mt.controls = true;
    mt.src = url;
    hf.href = url;
    hf.download = `${mediaConfig.tag}${counter}${mediaConfig.ext}`;
    hf.innerHTML = `donwload ${hf.download}`;
    hf.click();
}

const sheltersBtn = document.getElementById('sheltersBtn');
sheltersBtn.addEventListener('click', function (e) {
    navigator.geolocation.getCurrentPosition((position) => {
        window.location = sheltersBtn.getAttribute('data-url') + `?latitude=${position.coords.latitude}&longitude=${position.coords.longitude}`
    })
})


// Navbar
document.querySelector('.navbar-toggler').addEventListener('click', (e) => {
    document.querySelector('.navbar-collapse').classList.toggle('show');
})
document.querySelector('.navbar-placeholder').addEventListener('click', (e) => {
    document.querySelector('.navbar-collapse').classList.toggle('show');
})
