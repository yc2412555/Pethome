<template>
  <div class="classfy-cat">
    <!-- <p class="classfy-dog-title">狗狗种类</p> -->
    <div class="cat-detail-header">
      <div class="cat-detail-header-left" @click="goBackConsul">
        <span class="icon">&#xe60e;</span>
      </div>
      <div class="cat-detail-header-middle">猫猫种类大全</div>
    </div>
    <ul class="classfy-list">
      <li
        v-for="cat in datalist"
        :key="cat.cat_id"
        class="classfy-list-item"
        @click="gotoDetail(cat.cati_id)"
      >
        <img :src="cat.cat_vari_img" />
        <span>{{cat.vari_name }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import * as ajax from "@/request";
export default {
  data() {
    return {
      datalist: []
    };
  },
  created() {
    ajax.getCats().then(resp => {
      //console.log(resp)
      this.datalist = resp.data;
      // console.log(this.datalist)
    });
  },
  methods: {
    gotoDetail(id) {
      this.$router.push(`/catdetail/${id}`);
    },
    goBackConsul() {
      this.$router.push("/consul");
    }
  }
};
</script>

<style lang='scss'>
.cat-detail-header {
  height: 50px;
  background-color: #6debfc;
  padding: 0 10px;
  box-sizing: border-box;
  line-height: 50px;
  color: #ffffff;
  display: flex;
  &-left {
    font-size: 20px;
  }
  &-middle {
    flex: 1;
    text-align: center;
  }
}
.classfy-list {
  display: flex;
  flex-direction: column;
  background: #ebe9ed;
  &-item {
    height: 40px;
    display: flex;
    line-height: 40px;
    border-bottom: 1px solid #dfdde0;
    img {
      padding: 0 15px 0 0;
      width: 40px;
      height: 40px;
    }
  }
}
.classfy-cat-title {
  height: 40px;
  text-align: center;
  line-height: 40px;
  font-size: 16px;
}
</style>
