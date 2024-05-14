package com.service;

import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.service.IService;
import com.utils.PageUtils;
import com.entity.DiscussjiaxiaoxinxiEntity;
import java.util.List;
import java.util.Map;
import com.entity.vo.DiscussjiaxiaoxinxiVO;
import org.apache.ibatis.annotations.Param;
import com.entity.view.DiscussjiaxiaoxinxiView;


/**
 * 驾校信息评论表
 *
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
public interface DiscussjiaxiaoxinxiService extends IService<DiscussjiaxiaoxinxiEntity> {

    PageUtils queryPage(Map<String, Object> params);
    
   	List<DiscussjiaxiaoxinxiVO> selectListVO(Wrapper<DiscussjiaxiaoxinxiEntity> wrapper);
   	
   	DiscussjiaxiaoxinxiVO selectVO(@Param("ew") Wrapper<DiscussjiaxiaoxinxiEntity> wrapper);
   	
   	List<DiscussjiaxiaoxinxiView> selectListView(Wrapper<DiscussjiaxiaoxinxiEntity> wrapper);
   	
   	DiscussjiaxiaoxinxiView selectView(@Param("ew") Wrapper<DiscussjiaxiaoxinxiEntity> wrapper);
   	
   	PageUtils queryPage(Map<String, Object> params,Wrapper<DiscussjiaxiaoxinxiEntity> wrapper);
   	

}

