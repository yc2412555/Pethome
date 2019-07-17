<template>
    <div class="classfy-dog">
        <!-- <p class="classfy-dog-title">狗狗种类</p> -->
        <div class="dog-detail-header">
            <div class="dog-detail-header-left" @click="goBackConsul">
                <span class="icon">&#xe60e;</span>
            </div>
            <div class="dog-detail-header-middle">
                狗狗种类大全
            </div>
        </div>
        <ul class="classfy-list">
            <li 
                v-for='dog in datalist'
                :key = dog.id
                class="classfy-list-item"
                @click="gotoDetail(dog.dog_vari_id)"
            >
                <img :src="dog.dog_vari_img" />
                <span>{{dog.dog_vari_name }}</span>
            </li>
        </ul>
    </div>
</template>

<script>
import * as ajax from '@/request'
export default {
    data() {
        return{
            datalist:[]
        }
    },
    created() {
        ajax.getDogs().then(resp => {
                //console.log(resp)
                this.datalist = resp.data;
                //console.log(this.datalist)
            })
            
    },
    methods: {
        gotoDetail(id) {
            this.$router.push(`/dogdetail/${id}`)
        },
        goBackConsul() {
            this.$router.push('/consul')
        }

    }
}
</script>

<style lang='scss'>
.dog-detail-header{
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
.classfy-list{
    display: flex;
    flex-direction: column;
    background: #ebe9ed;
    &-item{
        height: 40px;
        display: flex;
        line-height: 40px;
        border-bottom: 1px solid #dfdde0;
        img{
            padding: 0 15px 0 0;
            width: 40px;
            height: 40px;
        }
    }
}
.classfy-dog-title{
    height: 40px;
    text-align: center;
    line-height: 40px;
    font-size: 16px;
}
</style>
