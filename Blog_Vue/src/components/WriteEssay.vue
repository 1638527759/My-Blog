<template>
  <div class="content">
    <form action="post">
      <input type="text" />
      <textarea name="essay" id="essay"></textarea>
    </form>
  </div>
</template>

<script setup name="WriteEssay"></script>

<style scoped lang="scss">
* {
  padding: 0;
  margin: 0;
}

.content {
  position: fixed;
  left: 50%;
  transform: translate(-50%, 100%);
  z-index: 60;
  width: 500px;
  height: 200px;
  background-color: rgba(255, 255, 255, 0.5);
  border: solid 2px white;
  border-radius: 5px;

  form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
}
</style>
