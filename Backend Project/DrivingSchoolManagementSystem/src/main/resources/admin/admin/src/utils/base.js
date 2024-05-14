const base = {
    get() {
        return {
            url : "http://localhost:8080/springbooto2ehg/",
            name: "springbooto2ehg",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/springbooto2ehg/front/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "驾校管理系统"
        } 
    }
}
export default base
