function loadYoutubeVideos(query) {
    const videoContainer = document.getElementById('video-cointainer')
    videoContainer.innerHTML = '...';
    $.get('/videos?query=' + query, function(data) {
        videoContainer.innerHTML = '';
        data.items.forEach(function(item) {
            const videoFrame = document.createElement('iframe')
            videoFrame.src = 'https://www.youtube.com/embed/' + item.id.videoId
            videoFrame.width='480'
            videoFrame.height='360'
            videoFrame.frameborder='0'
            videoFrame.allow='accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share'
            videoFrame.allowFullscreen=true
            videoContainer.appendChild(videoFrame) 
        })
    })
}