package com.service;

import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.service.IService;
import com.utils.PageUtils;
import com.entity.JiaochexinxiEntity;
import java.util.List;
import java.util.Map;
import com.entity.vo.JiaochexinxiVO;
import org.apache.ibatis.annotations.Param;
import com.entity.view.JiaochexinxiView;


/**
 * 缴车信息
 *
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
public interface JiaochexinxiService extends IService<JiaochexinxiEntity> {

    PageUtils queryPage(Map<String, Object> params);
    
   	List<JiaochexinxiVO> selectListVO(Wrapper<JiaochexinxiEntity> wrapper);
   	
   	JiaochexinxiVO selectVO(@Param("ew") Wrapper<JiaochexinxiEntity> wrapper);
   	
   	List<JiaochexinxiView> selectListView(Wrapper<JiaochexinxiEntity> wrapper);
   	
   	JiaochexinxiView selectView(@Param("ew") Wrapper<JiaochexinxiEntity> wrapper);
   	
   	PageUtils queryPage(Map<String, Object> params,Wrapper<JiaochexinxiEntity> wrapper);
   	

}

