<template>
  <div class="container">
    <div class="box-1"></div>
    <br />
    <div class="box-2"></div>
  </div>
</template>

<script setup name="RightCard"></script>

<style scoped lang="scss">
.container {
  margin-top: 0;
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;

  .box-1 {
    top: 0;
    width: 100%;
    height: 60%;
    background-color: white;
    box-shadow: 4px 2px 4px #55555555;
    border-radius: 5px;
    margin: auto;
    margin-top: 0;
  }

  .box-2 {
    top: 0;
    width: 100%;
    height: 100%;
    background-color: white;
    box-shadow: 4px 2px 4px #55555555;
    border-radius: 5px;
    margin: auto;
    margin-top: 0;
  }
}
</style>
