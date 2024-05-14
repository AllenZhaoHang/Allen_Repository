import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
import adminexam from '@/views/modules/exampaperlist/exam'
    import kaoshiyuyue from '@/views/modules/kaoshiyuyue/list'
    import yuyuelianche from '@/views/modules/yuyuelianche/list'
    import examfailrecord from '@/views/modules/examfailrecord/list'
    import qingjiashenqing from '@/views/modules/qingjiashenqing/list'
    import jiaochexinxi from '@/views/modules/jiaochexinxi/list'
    import examquestion from '@/views/modules/examquestion/list'
    import xueyuan from '@/views/modules/xueyuan/list'
    import jiaolianfenpei from '@/views/modules/jiaolianfenpei/list'
    import exampaperlist from '@/views/modules/exampaperlist/list'
    import genghuanjiaolian from '@/views/modules/genghuanjiaolian/list'
    import jiaxiaoxinxi from '@/views/modules/jiaxiaoxinxi/list'
    import examrecord from '@/views/modules/examrecord/list'
    import discussjiaxiaoxinxi from '@/views/modules/discussjiaxiaoxinxi/list'
    import news from '@/views/modules/news/list'
    import jiaolian from '@/views/modules/jiaolian/list'
    import kechenganpai from '@/views/modules/kechenganpai/list'
    import caiwuxinxi from '@/views/modules/caiwuxinxi/list'
    import exampaper from '@/views/modules/exampaper/list'
    import menu from '@/views/modules/menu/list'
    import ziyuanbeifen from '@/views/modules/ziyuanbeifen/list'
    import forum from '@/views/modules/forum/list'
    import baomingxinxi from '@/views/modules/baomingxinxi/list'
    import messages from '@/views/modules/messages/list'
    import cheliangxinxi from '@/views/modules/cheliangxinxi/list'
    import kaoqindaka from '@/views/modules/kaoqindaka/list'
    import config from '@/views/modules/config/list'
    import quxiaokecheng from '@/views/modules/quxiaokecheng/list'


//2.配置路由   注意：名字
const routes = [{
    path: '/index',
    name: '首页',
    component: Index,
    children: [{
      // 这里不设置值，是把main作为默认页面
      path: '/',
      name: '首页',
      component: Home,
      meta: {icon:'', title:'center'}
    }, {
      path: '/updatePassword',
      name: '修改密码',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: '支付',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: '个人信息',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/kaoshiyuyue',
        name: '考试预约',
        component: kaoshiyuyue
      }
      ,{
	path: '/yuyuelianche',
        name: '预约练车',
        component: yuyuelianche
      }
      ,{
	path: '/examfailrecord',
        name: '错题本',
        component: examfailrecord
      }
      ,{
	path: '/qingjiashenqing',
        name: '请假申请',
        component: qingjiashenqing
      }
      ,{
	path: '/jiaochexinxi',
        name: '缴车信息',
        component: jiaochexinxi
      }
      ,{
	path: '/examquestion',
        name: '试题管理',
        component: examquestion
      }
      ,{
	path: '/xueyuan',
        name: '学员',
        component: xueyuan
      }
      ,{
	path: '/jiaolianfenpei',
        name: '教练分配',
        component: jiaolianfenpei
      }
      ,{
	path: '/exampaperlist',
        name: '练习题库列表',
        component: exampaperlist
      }
      ,{
	path: '/genghuanjiaolian',
        name: '更换教练',
        component: genghuanjiaolian
      }
      ,{
	path: '/jiaxiaoxinxi',
        name: '驾校信息',
        component: jiaxiaoxinxi
      }
      ,{
	path: '/examrecord',
        name: '考试记录',
        component: examrecord
      }
      ,{
	path: '/discussjiaxiaoxinxi',
        name: '驾校信息评论',
        component: discussjiaxiaoxinxi
      }
      ,{
	path: '/news',
        name: '新闻公告',
        component: news
      }
      ,{
	path: '/jiaolian',
        name: '教练',
        component: jiaolian
      }
      ,{
	path: '/kechenganpai',
        name: '课程安排',
        component: kechenganpai
      }
      ,{
	path: '/caiwuxinxi',
        name: '财务信息',
        component: caiwuxinxi
      }
      ,{
	path: '/exampaper',
        name: '练习题库管理',
        component: exampaper
      }
      ,{
	path: '/menu',
        name: '菜单列表',
        component: menu
      }
      ,{
	path: '/ziyuanbeifen',
        name: '资源备份',
        component: ziyuanbeifen
      }
      ,{
	path: '/forum',
        name: '论坛交流',
        component: forum
      }
      ,{
	path: '/baomingxinxi',
        name: '报名信息',
        component: baomingxinxi
      }
      ,{
	path: '/messages',
        name: '留言反馈',
        component: messages
      }
      ,{
	path: '/cheliangxinxi',
        name: '车辆信息',
        component: cheliangxinxi
      }
      ,{
	path: '/kaoqindaka',
        name: '考勤打卡',
        component: kaoqindaka
      }
      ,{
	path: '/config',
        name: '轮播图管理',
        component: config
      }
      ,{
	path: '/quxiaokecheng',
        name: '取消课程',
        component: quxiaokecheng
      }
    ]
  },
  {
    path: '/adminexam',
    name: 'adminexam',
    component: adminexam,
    meta: {icon:'', title:'adminexam'}
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '/',
    name: '首页',
    redirect: '/index'
  }, /*默认跳转路由*/
  {
    path: '*',
    component: NotFound
  }
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
  mode: 'hash',
  /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})

export default router;
