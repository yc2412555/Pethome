<template>
  <div v-if="dogDeatil.dog_vari_name">
    <div class="dog-detail-header">
      <div class="dog-detail-header-left" @click="goBackToClassfy">
        <span class="icon">&#xe60e;</span>
      </div>
      <div class="dog-detail-header-middle">{{dogDeatil.dog_vari_name}}</div>
      <div class="dog-detail-header-right">分享</div>
    </div>
    <div class="dog-detail-content">
      <div class="dog-detail-content-mainimg" v-if="dogDeatil.photo">
        <img :src="dogDeatil.photo[0].dp_path" alt />
      </div>
      <div class="dog-detail-content-desc">
        <p v-cloak>中文名：{{dogDeatil.dog_vari_name}}</p>
        <p>英文名：{{dogDeatil.en_name}}</p>
        <p>别名：{{dogDeatil.alias}}</p>
        <p>生源地：{{dogDeatil.origin}}</p>
        <p>体型：{{dogDeatil.shape}}</p>
        <p>价格：{{dogDeatil.price}}元</p>
        <p>体重：{{dogDeatil.weight}}公斤</p>
        <p>
          黏人程度:
          <span
            class="icon rate-star"
            v-for=" index in dogDeatil.sti_degree"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <p>
          喜叫程度:
          <span
            class="icon rate-star"
            v-for=" index in dogDeatil.bar_degree"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <p>
          掉毛程度:
          <span
            class="icon rate-star"
            v-for=" index in dogDeatil.hairloss_degree"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <p>
          对小孩友善程度:
          <span
            class="icon rate-star"
            v-for=" index in dogDeatil.fri_degree"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <p>
          对陌生人友善程度:
          <span
            class="icon rate-star"
            v-for=" index in dogDeatil.stranger_fri_degree"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <p>
          服从度:
          <span
            class="icon rate-star"
            v-for=" index in dogDeatil.compliance"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <p>
          护家程度:
          <span
            class="icon rate-star"
            v-for=" index in dogDeatil.home_degree"
            :key="index"
          >&#xe6c2;</span>
        </p>
        <div class="dog-detail-content-desc-other">
          品种特点：
          <b>{{dogDeatil.feature}}</b>
        </div>
        <div class="dog-detail-content-desc-other">注意事项：{{dogDeatil.attention}}</div>
        <div class="dog-detail-content-desc-other">养宠知识：{{dogDeatil.nurturing_knowledge}}</div>
      </div>
    </div>
  </div>
  <div v-else></div>
</template>

<script>
import * as ajax from "@/request"
export default {
  created() {
    this.getDetailId();
    ajax.getDogDetail(this.dogId).then(resp => {
      this.dogDeatil = resp
      //console.log(this.dogDeatil)
    })
  },
  data() {
    return {
      dogId: null,
      dogDeatil: {}
    }
  },
  methods: {
    getDetailId() {
      this.dogId = this.$route.params.id
    },
    goBackToClassfy() {
      this.$router.push("/classfydog")
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
