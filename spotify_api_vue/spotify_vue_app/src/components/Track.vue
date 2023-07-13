
<template>
  <div class="track-component">
    <div class="image-container">
      <img :src="track.album_image" alt="Album Image" class="album-image">
    </div>
    <div class="track-info">
      <h3 class="track-name">{{ track.track_name }}</h3>
      <p class="artist-name">{{ track.artist_name }}</p>
    </div>
    <div class="audio">
        <audio controls>
            <source :src="track.preview_url" type="audio/mpeg" />
        </audio>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    track: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped>
.track-component {
  display: flex;
  align-items: center;
  background-color: #254e70;
  height: 100px;
  width: 1000px;
  margin-bottom: 10px;
  border: 2px solid #37718e;
  border-radius: 8px;
}

.image-container {
  margin: 0 30px;
}

.album-image {
  width: 96px;
  height: 96px;
}

.track-info {
  flex-grow: 1;
}

.track-name {
  font-weight: bold;
  font-size: 24px;
  margin-bottom: 4px;
  color: #ffffff;
}

.artist-name {
  font-size: 18px;
  color: #ffffff;
}
.audio{
    margin-right: 20px;
}
.play-button {
  background-color: transparent;
  border: none;
  width: 30px;
  height: 30px;
  margin-right: 20px;
  background-image: url('../assets/play-button.png'); 
  background-size: cover;
  cursor: pointer;
}
</style>
