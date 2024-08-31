<script setup lang="ts">
  import { redirectToSpotifyAuthorize } from '../auth/auth'

</script>

<template>
  <main>
      <button @click="redirectToSpotifyAuthorize()">Log in with Spotify</button>
  </main>
</template>
