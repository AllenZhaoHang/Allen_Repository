
var projectName = '驾校管理系统';
/**
 * 轮播图配置
 */
var swiper = {
	// 设定轮播容器宽度，支持像素和百分比
	width: '100%',
	height: '400px',
	// hover（悬停显示）
	// always（始终显示）
	// none（始终不显示）
	arrow: 'none',
	// default（左右切换）
	// updown（上下切换）
	// fade（渐隐渐显切换）
	anim: 'default',
	// 自动切换的时间间隔
	// 默认3000
	interval: 2000,
	// 指示器位置
	// inside（容器内部）
	// outside（容器外部）
	// none（不显示）
	indicator: 'outside'
}

/**
 * 个人中心菜单
 */
var centerMenu = [{
	name: '个人中心',
	url: '../' + localStorage.getItem('userTable') + '/center.html'
}, 
{
	name: '我的发布',
	url: '../forum/list-my.html'
},

{
	name: '考试记录',
	url: '../examrecord/list.html'
}, 
{
	name: '错题本',
	url: '../examrecord/wrong.html'
},
{
        name: '我的收藏',
        url: '../storeup/list.html'
}
]


var indexNav = [

{
	name: '驾校信息',
	url: './pages/jiaxiaoxinxi/list.html'
}, 
{
	name: '车辆信息',
	url: './pages/cheliangxinxi/list.html'
}, 

{
	name: '论坛交流',
	url: './pages/forum/list.html'
}, 
{
	name: '练习题库',
	url: './pages/exampaper/list.html'
}, 
{
	name: '新闻公告',
	url: './pages/news/list.html'
},
{
	name: '留言反馈',
	url: './pages/messages/list.html'
}
]

var adminurl =  "http://localhost:8080/springbooto2ehg/admin/dist/index.html";

var cartFlag = false

var chatFlag = false




var menu = [{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-rank","buttons":["新增","查看","修改","删除"],"menu":"学员","menuJump":"列表","tableName":"xueyuan"}],"menu":"学员管理"},{"child":[{"appFrontIcon":"cuIcon-brand","buttons":["新增","查看","修改","删除"],"menu":"教练","menuJump":"列表","tableName":"jiaolian"}],"menu":"教练管理"},{"child":[{"appFrontIcon":"cuIcon-discover","buttons":["新增","查看","修改","删除","查看评论","报名"],"menu":"驾校信息","menuJump":"列表","tableName":"jiaxiaoxinxi"}],"menu":"驾校信息管理"},{"child":[{"appFrontIcon":"cuIcon-copy","buttons":["查看","删除","审核","报表","教练分配"],"menu":"报名信息","menuJump":"列表","tableName":"baomingxinxi"}],"menu":"报名信息管理"},{"child":[{"appFrontIcon":"cuIcon-similar","buttons":["新增","查看","修改","删除"],"menu":"车辆信息","menuJump":"列表","tableName":"cheliangxinxi"}],"menu":"车辆信息管理"},{"child":[{"appFrontIcon":"cuIcon-time","buttons":["查看","修改","删除"],"menu":"教练分配","menuJump":"列表","tableName":"jiaolianfenpei"}],"menu":"教练分配管理"},{"child":[{"appFrontIcon":"cuIcon-wenzi","buttons":["查看","删除","审核"],"menu":"更换教练","menuJump":"列表","tableName":"genghuanjiaolian"}],"menu":"更换教练管理"},{"child":[{"appFrontIcon":"cuIcon-time","buttons":["查看","删除"],"menu":"课程安排","menuJump":"列表","tableName":"kechenganpai"}],"menu":"课程安排管理"},{"child":[{"appFrontIcon":"cuIcon-phone","buttons":["查看","删除"],"menu":"取消课程","menuJump":"列表","tableName":"quxiaokecheng"}],"menu":"取消课程管理"},{"child":[{"appFrontIcon":"cuIcon-link","buttons":["查看","删除","审核"],"menu":"考试预约","menuJump":"列表","tableName":"kaoshiyuyue"}],"menu":"考试预约管理"},{"child":[{"appFrontIcon":"cuIcon-time","buttons":["查看","删除","审核"],"menu":"考勤打卡","menuJump":"列表","tableName":"kaoqindaka"}],"menu":"考勤打卡管理"},{"child":[{"appFrontIcon":"cuIcon-phone","buttons":["查看","删除","审核"],"menu":"请假申请","menuJump":"列表","tableName":"qingjiashenqing"}],"menu":"请假申请管理"},{"child":[{"appFrontIcon":"cuIcon-time","buttons":["查看","删除","审核"],"menu":"缴车信息","menuJump":"列表","tableName":"jiaochexinxi"}],"menu":"缴车信息管理"},{"child":[{"appFrontIcon":"cuIcon-pic","buttons":["新增","查看","修改","删除"],"menu":"资源备份","menuJump":"列表","tableName":"ziyuanbeifen"}],"menu":"资源备份管理"},{"child":[{"appFrontIcon":"cuIcon-list","buttons":["新增","查看","修改","删除"],"menu":"财务信息","menuJump":"列表","tableName":"caiwuxinxi"}],"menu":"财务信息管理"},{"child":[{"appFrontIcon":"cuIcon-group","buttons":["查看","修改","删除"],"menu":"论坛交流","tableName":"forum"}],"menu":"论坛交流"},{"child":[{"appFrontIcon":"cuIcon-copy","buttons":["新增","查看","修改","删除"],"menu":"练习题库管理","tableName":"exampaper"}],"menu":"练习题库管理"},{"child":[{"appFrontIcon":"cuIcon-message","buttons":["查看","修改","回复","删除"],"menu":"留言反馈","tableName":"messages"}],"menu":"留言反馈"},{"child":[{"appFrontIcon":"cuIcon-taxi","buttons":["新增","查看","修改","删除"],"menu":"试题管理","tableName":"examquestion"}],"menu":"试题管理"},{"child":[{"appFrontIcon":"cuIcon-wenzi","buttons":["查看","修改","删除"],"menu":"轮播图管理","tableName":"config"},{"appFrontIcon":"cuIcon-attentionfavor","buttons":["查看","编辑名称","编辑父级","删除"],"menu":"菜单列表","tableName":"menu"},{"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除"],"menu":"新闻公告","tableName":"news"}],"menu":"系统管理"},{"child":[{"appFrontIcon":"cuIcon-attentionfavor","buttons":["查看","删除"],"menu":"考试记录","tableName":"examrecord"},{"appFrontIcon":"cuIcon-brand","buttons":["查看","删除"],"menu":"错题本","tableName":"examfailrecord"}],"menu":"考试管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看","报名"],"menu":"驾校信息列表","menuJump":"列表","tableName":"jiaxiaoxinxi"}],"menu":"驾校信息模块"},{"child":[{"appFrontIcon":"cuIcon-form","buttons":["查看"],"menu":"车辆信息列表","menuJump":"列表","tableName":"cheliangxinxi"}],"menu":"车辆信息模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员","tableName":"users"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-copy","buttons":["查看","支付"],"menu":"报名信息","menuJump":"列表","tableName":"baomingxinxi"}],"menu":"报名信息管理"},{"child":[{"appFrontIcon":"cuIcon-time","buttons":["查看","更换教练","预约练车"],"menu":"教练分配","menuJump":"列表","tableName":"jiaolianfenpei"}],"menu":"教练分配管理"},{"child":[{"appFrontIcon":"cuIcon-wenzi","buttons":["查看","修改","删除"],"menu":"更换教练","menuJump":"列表","tableName":"genghuanjiaolian"}],"menu":"更换教练管理"},{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看","修改","删除"],"menu":"预约练车","menuJump":"列表","tableName":"yuyuelianche"}],"menu":"预约练车管理"},{"child":[{"appFrontIcon":"cuIcon-time","buttons":["查看","取消课程"],"menu":"课程安排","menuJump":"列表","tableName":"kechenganpai"}],"menu":"课程安排管理"},{"child":[{"appFrontIcon":"cuIcon-phone","buttons":["查看","修改","删除"],"menu":"取消课程","menuJump":"列表","tableName":"quxiaokecheng"}],"menu":"取消课程管理"},{"child":[{"appFrontIcon":"cuIcon-link","buttons":["新增","查看","修改","删除"],"menu":"考试预约","menuJump":"列表","tableName":"kaoshiyuyue"}],"menu":"考试预约管理"},{"child":[{"appFrontIcon":"cuIcon-baby","buttons":["查看"],"menu":"练习题库列表","tableName":"exampaperlist"},{"appFrontIcon":"cuIcon-attentionfavor","buttons":["查看"],"menu":"考试记录","tableName":"examrecord"},{"appFrontIcon":"cuIcon-brand","buttons":["查看"],"menu":"错题本","tableName":"examfailrecord"}],"menu":"考试管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看","报名"],"menu":"驾校信息列表","menuJump":"列表","tableName":"jiaxiaoxinxi"}],"menu":"驾校信息模块"},{"child":[{"appFrontIcon":"cuIcon-form","buttons":["查看"],"menu":"车辆信息列表","menuJump":"列表","tableName":"cheliangxinxi"}],"menu":"车辆信息模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"学员","tableName":"xueyuan"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看","审核","课程安排"],"menu":"预约练车","menuJump":"列表","tableName":"yuyuelianche"}],"menu":"预约练车管理"},{"child":[{"appFrontIcon":"cuIcon-time","buttons":["查看","修改","删除"],"menu":"课程安排","menuJump":"列表","tableName":"kechenganpai"}],"menu":"课程安排管理"},{"child":[{"appFrontIcon":"cuIcon-phone","buttons":["查看","审核"],"menu":"取消课程","menuJump":"列表","tableName":"quxiaokecheng"}],"menu":"取消课程管理"},{"child":[{"appFrontIcon":"cuIcon-time","buttons":["新增","查看","修改","删除"],"menu":"考勤打卡","menuJump":"列表","tableName":"kaoqindaka"}],"menu":"考勤打卡管理"},{"child":[{"appFrontIcon":"cuIcon-phone","buttons":["新增","查看","修改","删除"],"menu":"请假申请","menuJump":"列表","tableName":"qingjiashenqing"}],"menu":"请假申请管理"},{"child":[{"appFrontIcon":"cuIcon-time","buttons":["新增","查看","修改","删除"],"menu":"缴车信息","menuJump":"列表","tableName":"jiaochexinxi"}],"menu":"缴车信息管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-newshot","buttons":["查看","报名"],"menu":"驾校信息列表","menuJump":"列表","tableName":"jiaxiaoxinxi"}],"menu":"驾校信息模块"},{"child":[{"appFrontIcon":"cuIcon-form","buttons":["查看"],"menu":"车辆信息列表","menuJump":"列表","tableName":"cheliangxinxi"}],"menu":"车辆信息模块"}],"hasBackLogin":"是","hasBackRegister":"是","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"教练","tableName":"jiaolian"}]


var isAuth = function (tableName,key) {
    let role = localStorage.getItem("userTable");
    let menus = menu;
    for(let i=0;i<menus.length;i++){
        if(menus[i].tableName==role){
            for(let j=0;j<menus[i].backMenu.length;j++){
                for(let k=0;k<menus[i].backMenu[j].child.length;k++){
                    if(tableName==menus[i].backMenu[j].child[k].tableName){
                        let buttons = menus[i].backMenu[j].child[k].buttons.join(',');
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        }
    }
    return false;
}

var isFrontAuth = function (tableName,key) {
    let role = localStorage.getItem("userTable");
    let menus = menu;
    for(let i=0;i<menus.length;i++){
        if(menus[i].tableName==role){
            for(let j=0;j<menus[i].frontMenu.length;j++){
                for(let k=0;k<menus[i].frontMenu[j].child.length;k++){
                    if(tableName==menus[i].frontMenu[j].child[k].tableName){
                        let buttons = menus[i].frontMenu[j].child[k].buttons.join(',');
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        }
    }
    return false;
}
