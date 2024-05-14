package com.service;

import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.service.IService;
import com.utils.PageUtils;
import com.entity.JiaxiaoxinxiEntity;
import java.util.List;
import java.util.Map;
import com.entity.vo.JiaxiaoxinxiVO;
import org.apache.ibatis.annotations.Param;
import com.entity.view.JiaxiaoxinxiView;


/**
 * 驾校信息
 *
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public interface JiaxiaoxinxiService extends IService<JiaxiaoxinxiEntity> {

    PageUtils queryPage(Map<String, Object> params);
    
   	List<JiaxiaoxinxiVO> selectListVO(Wrapper<JiaxiaoxinxiEntity> wrapper);
   	
   	JiaxiaoxinxiVO selectVO(@Param("ew") Wrapper<JiaxiaoxinxiEntity> wrapper);
   	
   	List<JiaxiaoxinxiView> selectListView(Wrapper<JiaxiaoxinxiEntity> wrapper);
   	
   	JiaxiaoxinxiView selectView(@Param("ew") Wrapper<JiaxiaoxinxiEntity> wrapper);
   	
   	PageUtils queryPage(Map<String, Object> params,Wrapper<JiaxiaoxinxiEntity> wrapper);
   	

}

