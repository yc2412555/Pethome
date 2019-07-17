<template>
  <div v-if=" catDeatil.vari_name">
    <div class="dog-detail-header">
      <div class="dog-detail-header-left" @click="goBackToClassfy">
        <span class="icon">&#xe60e;</span>
      </div>
      <div class="dog-detail-header-middle">{{ catDeatil.vari_name}}</div>
      <div class="dog-detail-header-right">分享</div>
    </div>
    <div class="dog-detail-content">
      <div class="dog-detail-content-mainimg" v-if=" catDeatil.photos">
        <img :src=" catDeatil.photos[0].dp_path" alt />
      </div>
      <div class="dog-detail-content-desc">
        <p v-cloak>中文名：{{ catDeatil.vari_name}}</p>
        <p>英文名：{{ catDeatil.en_name}}</p>
        <p>别名：{{ catDeatil.alias}}</p>
        <p>生源地：{{ catDeatil.origin}}</p>
        <p>体型：{{ catDeatil.shape}}</p>
        <p>价格：{{ catDeatil.price}}元</p>
        <p>体重：{{ catDeatil.weight}}公斤</p>
        <p>
          黏人程度:
          <span
            class="icon rate-star"
            v-for=" index in  catDeatil.sti_degree"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <p>
          喜叫程度:
          <span
            class="icon rate-star"
            v-for=" index in  catDeatil.bar_degree"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <p>
          掉毛程度:
          <span
            class="icon rate-star"
            v-for=" index in  catDeatil.hairloss_degree"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <p>
          对小孩友善程度:
          <span
            class="icon rate-star"
            v-for=" index in  catDeatil.fri_degree"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <p>
          可训练性:
          <span
            class="icon rate-star"
            v-for=" index in  catDeatil.trainability"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <p>
          城市适应性:
          <span
            class="icon rate-star"
            v-for=" index in  catDeatil.city_degree"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <div class="dog-detail-content-desc-other">猫咪习性：{{ catDeatil.cat_habbit}}</div>
        <div class="dog-detail-content-desc-other">
          品种特点：
          <b>{{ catDeatil.feature}}</b>
        </div>
        <div class="dog-detail-content-desc-other">注意事项：{{ catDeatil.attention}}</div>
        <div class="dog-detail-content-desc-other">养宠知识：{{ catDeatil.nurturing_knowledge}}</div>
      </div>
    </div>
  </div>
  <div v-else></div>
</template>

<script>
import * as ajax from "@/request"
export default {
  created() {
    this.getDetailId()
    ajax.getCatDetail(this.catId).then(resp => {
      this.catDeatil = resp
    })
  },
  data() {
    return {
      catId: null,
      catDeatil: {}
    }
  },
  methods: {
    getDetailId() {
      this.catId = this.$route.params.id
    },
    goBackToClassfy() {
      this.$router.push("/classfycat");
    }
  }
}
</script>

<style lang='scss' scoped>
[v-cloak] {
  display: none;
}
.dog-detail-header {
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
.dog-detail-content {
  padding: 10px;
  box-sizing: border-box;
  &-mainimg {
    width: 100%;
    height: 150px;
    img {
      width: 100%;
      height: 100%;
    }
  }
  &-desc {
    padding-top: 10px;
    box-sizing: border-box;
    & > p {
      height: 30px;
      padding: 5px 0;
      box-sizing: border-box;
      .rate-star {
        color: red;
      }
    }
    &-other {
      padding: 5px 0;
      box-sizing: border-box;
      & > b {
        line-height: 10px;
      }
    }
  }
}
</style>
