<template>
<div class="container-fluid">
    <div class="header">
      <img class="logo" src="./assets/spotify.png" alt="Spotify Logo" />
      <h2 class="title">Search Popular Tracks from a Genre</h2>
    </div>
    <div class="search-bar mx-auto">
      <div class="input-group">
        <input type="text" class="form-control" v-model="genre" placeholder="Search a genre">
        <div class="input-group-append">
          <button class="btn btn-light" type="button" @click="searchTopTracks">
            <img src="./assets/search2.png" alt="" width="24" height="24">
          </button>
        </div>
      </div>
    </div>
    <div class="tracks-container">
      <Track v-for="track in tracks" :key="track.track_name" :track="track" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Track from './components/Track.vue';

export default {
  components: {
    Track
  },
  data() {
    return {
      genre: '',
      tracks: [],
    };
  },
  methods: {
    searchTopTracks() {
        this.genre = this.genre.toLowerCase();
        
        axios.get(`http://127.0.0.1:8000/api/v1/tracks/${encodeURIComponent(this.genre)}/`)
          .then(response => {
            //const tracks = response.data;
            //console.log('Track List:', tracks);
            this.tracks = response.data;
          })
          .catch(error => {
            console.error(error);
          });
    },
  },
};
</script>

<style>
body {
  background: #aef3e7;
  background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#5bc0be), color-stop(100%,#37718e));
  background: -webkit-linear-gradient(top,  #aef3e7 0%, #37718e 100%);
  background:    -moz-linear-gradient(top,  #aef3e7 0%, #37718e 100%);
  background:     -ms-linear-gradient(top,  #aef3e7 0%, #37718e 100%);
  background:      -o-linear-gradient(top,  #aef3e7 0%, #37718e 100%);
  background:         linear-gradient(to bottom, #aef3e7 0%, #37718e 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#aef3e7', endColorstr='#37718e',GradientType=0 );
  background-attachment: fixed;
}

.container-fluid {
  padding: 20px;
  color: #ffffff;
}

.header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.logo {
  width: 40px;
  height: 40px;
  margin-right: 10px;
}

.title {
  font-size: 24px;
  font-weight: bold;
}

.search-bar {
  margin-bottom: 20px;
  width: 300px;

}


.tracks-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input-group {
  width: 300px;
}

.input-group-append {
  position: relative;
}

.input-group-append .btn {
  position: absolute;
  top: 0;
  right: 0;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.form-control {
  height: 40px;
  font-size: 16px;
}



</style>
