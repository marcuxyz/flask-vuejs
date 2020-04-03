<template>
  <div id="presentation">
    <h1>Apresentation</h1>
    Hello {{name}}
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "HelloWorld",
  props: [
    "name"
  ]
};
</script>
