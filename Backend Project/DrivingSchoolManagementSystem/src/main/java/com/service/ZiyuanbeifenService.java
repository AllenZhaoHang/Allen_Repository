package com.service;

import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.service.IService;
import com.utils.PageUtils;
import com.entity.ZiyuanbeifenEntity;
import java.util.List;
import java.util.Map;
import com.entity.vo.ZiyuanbeifenVO;
import org.apache.ibatis.annotations.Param;
import com.entity.view.ZiyuanbeifenView;


/**
 * 资源备份
 *
 * @author 
 * @email 
 * @date 2022-04-20 00:17:37
 */
public interface ZiyuanbeifenService extends IService<ZiyuanbeifenEntity> {

    PageUtils queryPage(Map<String, Object> params);
    
   	List<ZiyuanbeifenVO> selectListVO(Wrapper<ZiyuanbeifenEntity> wrapper);
   	
   	ZiyuanbeifenVO selectVO(@Param("ew") Wrapper<ZiyuanbeifenEntity> wrapper);
   	
   	List<ZiyuanbeifenView> selectListView(Wrapper<ZiyuanbeifenEntity> wrapper);
   	
   	ZiyuanbeifenView selectView(@Param("ew") Wrapper<ZiyuanbeifenEntity> wrapper);
   	
   	PageUtils queryPage(Map<String, Object> params,Wrapper<ZiyuanbeifenEntity> wrapper);
   	

}

