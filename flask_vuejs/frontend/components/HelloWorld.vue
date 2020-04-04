<template>
  <div>
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
