<template>
  <div>
    <img :src="'http://' + hostname + ':' + port + '/?action=stream'" />
    <vue3-slider v-model="degree" height=25 color="#FB278D" track-color="#FEFEFE" />
  </div>
  <div>
    <button class="glow-on-hover" type="button" v-on:click="moveLeft">Left</button>
    <button class="glow-on-hover" type="button" v-on:click="moveLeft">Right</button>
  </div>
</template>
    
<script>
import axios from "axios";
import slider from "vue3-slider";
import _ from 'lodash';


export default {

    props: ['degree'],

    components: {
    "vue3-slider": slider
  },

      watch: { 
      	degree: _.debounce(function(newDegree) {
          console.log('wartosc' + newDegree)
          axios.get(`http://192.168.0.10/s1/${newDegree}`);
        }, 1000)
      },

  data() {
    return {
      hostname: location.hostname,
      port: 8080
    };
  },
  methods: {
    moveLeft: function (event) {
      axios.get("http://192.168.0.10/s2/left");
    },

    moveRight: function (event) {
      axios.get("http://192.168.0.10/s2/right");
    },
  },
};
</script>
<style>
html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    background: #000;
}

.glow-on-hover {
    width: 220px;
    height: 50px;
    border: none;
    outline: none;
    color: #fff;
    background: #111;
    cursor: pointer;
    position: relative;
    z-index: 0;
    border-radius: 10px;
    margin: 20px;
}

.glow-on-hover:before {
    content: '';
    background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
    position: absolute;
    top: -2px;
    left:-2px;
    background-size: 400%;
    z-index: -1;
    filter: blur(5px);
    width: calc(100% + 4px);
    height: calc(100% + 4px);
    animation: glowing 20s linear infinite;
    opacity: 0;
    transition: opacity .3s ease-in-out;
    border-radius: 10px;
}

.glow-on-hover:active {
    color: #000
}

.glow-on-hover:active:after {
    background: transparent;
}

.glow-on-hover:hover:before {
    opacity: 1;
}

.glow-on-hover:after {
    z-index: -1;
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: #111;
    left: 0;
    top: 0;
    border-radius: 10px;
}

@keyframes glowing {
    0% { background-position: 0 0; }
    50% { background-position: 400% 0; }
    100% { background-position: 0 0; }
}
</style>