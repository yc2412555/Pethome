<template>
  <div class="consul-wrapper">
    <div class="dog-consul-header">
      <div class="dog-consul-header-middle">
          宠物百科
      </div>
    </div>
    <p class="baike-item" @click="goToDogItem">
      汪星人百科
    </p>
    <p class="baike-item" @click="goToCatItem">
      喵星人百科
    </p>
  </div> 
</template>

<script>
export default {
  data() {
    return{

    }
  },
  methods: {
    goToDogItem() {
      this.$router.push('/classfydog')
    },
    goToCatItem() {
      this.$router.push('/classfycat')
    }
  }
}
</script>

<style lang='scss' scoped>
.dog-consul-header{
    height: 50px;
    background-color: #6DEBFC;
    padding: 0 10px;
    box-sizing: border-box;
    line-height: 50px;
    color: #ffffff;
    display: flex;
    &-left{
        font-size: 20px;
    }
    &-middle{
        flex: 1;
        text-align: center;
    }
}

.baike-item{
  padding: 10px 0;
  height: 200px;
  line-height: 200px;
  text-align: center;
  box-sizing: border-box;
  background: #f2f2f2;
  margin: 40px 0;
  //color: #ffffff;
}
  
</style>
