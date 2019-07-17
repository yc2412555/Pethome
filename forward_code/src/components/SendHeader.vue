<template>
  <div>
    <mt-header title="发送动态">
      <mt-button icon="back" slot="left" @click="goBack">返回</mt-button>
      <!-- <mt-button icon="more" slot="right"></mt-button> -->
    </mt-header>
  </div>
</template>

<script>
export default {
  methods: {
    goBack() {
      this.$router.go(-1)
    }
  }
};
</script>

<style>
.mint-header {
  background-color: rgb(109, 235, 252);
}
</style>
