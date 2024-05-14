package com.service;

import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.service.IService;
import com.utils.PageUtils;
import com.entity.GenghuanjiaolianEntity;
import java.util.List;
import java.util.Map;
import com.entity.vo.GenghuanjiaolianVO;
import org.apache.ibatis.annotations.Param;
import com.entity.view.GenghuanjiaolianView;


/**
 * 更换教练
 *
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public interface GenghuanjiaolianService extends IService<GenghuanjiaolianEntity> {

    PageUtils queryPage(Map<String, Object> params);
    
   	List<GenghuanjiaolianVO> selectListVO(Wrapper<GenghuanjiaolianEntity> wrapper);
   	
   	GenghuanjiaolianVO selectVO(@Param("ew") Wrapper<GenghuanjiaolianEntity> wrapper);
   	
   	List<GenghuanjiaolianView> selectListView(Wrapper<GenghuanjiaolianEntity> wrapper);
   	
   	GenghuanjiaolianView selectView(@Param("ew") Wrapper<GenghuanjiaolianEntity> wrapper);
   	
   	PageUtils queryPage(Map<String, Object> params,Wrapper<GenghuanjiaolianEntity> wrapper);
   	

}

