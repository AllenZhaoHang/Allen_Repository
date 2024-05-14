package com.service;

import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.service.IService;
import com.utils.PageUtils;
import com.entity.YuyueliancheEntity;
import java.util.List;
import java.util.Map;
import com.entity.vo.YuyueliancheVO;
import org.apache.ibatis.annotations.Param;
import com.entity.view.YuyueliancheView;


/**
 * 预约练车
 *
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public interface YuyueliancheService extends IService<YuyueliancheEntity> {

    PageUtils queryPage(Map<String, Object> params);
    
   	List<YuyueliancheVO> selectListVO(Wrapper<YuyueliancheEntity> wrapper);
   	
   	YuyueliancheVO selectVO(@Param("ew") Wrapper<YuyueliancheEntity> wrapper);
   	
   	List<YuyueliancheView> selectListView(Wrapper<YuyueliancheEntity> wrapper);
   	
   	YuyueliancheView selectView(@Param("ew") Wrapper<YuyueliancheEntity> wrapper);
   	
   	PageUtils queryPage(Map<String, Object> params,Wrapper<YuyueliancheEntity> wrapper);
   	

}

