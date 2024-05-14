package com.service;

import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.service.IService;
import com.utils.PageUtils;
import com.entity.JiaolianfenpeiEntity;
import java.util.List;
import java.util.Map;
import com.entity.vo.JiaolianfenpeiVO;
import org.apache.ibatis.annotations.Param;
import com.entity.view.JiaolianfenpeiView;


/**
 * 教练分配
 *
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public interface JiaolianfenpeiService extends IService<JiaolianfenpeiEntity> {

    PageUtils queryPage(Map<String, Object> params);
    
   	List<JiaolianfenpeiVO> selectListVO(Wrapper<JiaolianfenpeiEntity> wrapper);
   	
   	JiaolianfenpeiVO selectVO(@Param("ew") Wrapper<JiaolianfenpeiEntity> wrapper);
   	
   	List<JiaolianfenpeiView> selectListView(Wrapper<JiaolianfenpeiEntity> wrapper);
   	
   	JiaolianfenpeiView selectView(@Param("ew") Wrapper<JiaolianfenpeiEntity> wrapper);
   	
   	PageUtils queryPage(Map<String, Object> params,Wrapper<JiaolianfenpeiEntity> wrapper);
   	

}

