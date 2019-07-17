<template>
    <div>
      <ul class="cyq-footer">
        <router-link 
          tag="li"
          v-for="tabbar in tabbars"
          :key="tabbar.name"
          :to="tabbar.path"
        >
          <i class="icon" v-html="tabbar.meta.icon"></i>
          <span>{{tabbar.meta.title}}</span>
        </router-link>
      </ul>
    </div>
</template>

<script>
import routes from '@/router/routes'
export default {
  data () {
    return {
      tabbars: routes.filter(route => route.meta.isTabbar)
    }
  }
}
</script>

<style lang="scss" scoped>
$mainColor: rgb(109, 235, 252);
.cyq-footer {
  display: flex;
  height: 52px;
  border-top: 1px solid #dedede;
  justify-content: space-around;
  text-align: center;
  .router-link-exact-active,
  .router-link-active {
    color: $mainColor;
  }
  i {
    display: block;
    font-size: 24px;
    line-height: 32px;
  }
  span {
    font-size: 12px;
    line-height: 20px;
  }
}
</style>
