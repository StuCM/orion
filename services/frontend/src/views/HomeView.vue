<script setup lang="ts">
  import { onMounted } from 'vue';
import { redirectToSpotifyAuthorize, checkForToken } from '../auth/auth'

  onMounted(() => {
    checkForToken()
  })

</script>

<template>
  <main>
      <button @click="redirectToSpotifyAuthorize()">Log in with Spotify</button>
  </main>
</template>
