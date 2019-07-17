<template>
  <div class="cyq-favour-main">
    <!-- <div class="cyq-favour-main-header">
      <h1>宠友圈</h1>
    </div> -->
    <div class="cyq-favour-main-list">
      <ul>
        <CyqFavourItem
          v-for="item in list"
          :key="item.d_id"
          :id="item.d_id"
          :comments="item.comments"
          :g_counts="item.g_counts"
          :path="item.path"
          :pub_time="item.pub_time"
          :text_content="item.text_content"
          :user="item.user"
          @sendSuccess="sendSuccess"
          class="CyqFavourItem"
        ></CyqFavourItem>
      </ul>
    </div>
    <div class="cyq-favour-main-aside">
      <span class="cyq-favour-main-aside-button" @click.stop="sendDynamic({})">发布</span>
    </div>
  </div>
</template>

<script>
import * as ajax from "@/request/index"
import CyqFavourItem from "@/components/CyqFavourItem"

export default {
  data() {
    return {
      list: []
    }
  },
  components: {
    CyqFavourItem
  },
  methods: {
    sendDynamic() {
      this.$router.push("/send")
    },
    getData() {
      ajax.getDynamics().then(resp => {
        this.list = resp.data.results
      })
    },
    sendSuccess(value) {
      if(value ===200 ){
        this.getData()
      }
    }
  },
  created() {
    this.getData()
  }
}
</script>

<style lang="scss" scoped>
  .cyq-favour-main {
    // height: 100%;
    // position: relative;
    background: #f4f4f4;
    display: flex;
    flex-direction: column;

    &-header {
      background: #ffffff;
      line-height: 50px;
      text-align: center;
      font-size: 18px;
      height: 50px;
      margin-bottom: 10px;
    }
    
    &-list {
    //  height: 100%;
     ul {
       .CyqFavourItem {
          // height: 350px;
          margin-bottom: 10px;
          padding: 0 15px;
       }
     }
    }

    &-aside {
      position: fixed;
      bottom: 80px;
      right: 10px;

      &-button {
        display: block;
        width: 40px;
        height: 40px;
        background: rgb(234, 251, 253);
        border: 1px solid rgb(109, 235, 252);
        border-radius: 50%;
        text-align: center;
        line-height: 40px;
        color: rgb(109, 235, 252);
        color: #333;
        font-family: "幼圆";
      }
    }
  }
</style>


