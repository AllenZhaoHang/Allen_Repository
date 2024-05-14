package com.service;

import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.service.IService;
import com.utils.PageUtils;
import com.entity.QuxiaokechengEntity;
import java.util.List;
import java.util.Map;
import com.entity.vo.QuxiaokechengVO;
import org.apache.ibatis.annotations.Param;
import com.entity.view.QuxiaokechengView;


/**
 * 取消课程
 *
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public interface QuxiaokechengService extends IService<QuxiaokechengEntity> {

    PageUtils queryPage(Map<String, Object> params);
    
   	List<QuxiaokechengVO> selectListVO(Wrapper<QuxiaokechengEntity> wrapper);
   	
   	QuxiaokechengVO selectVO(@Param("ew") Wrapper<QuxiaokechengEntity> wrapper);
   	
   	List<QuxiaokechengView> selectListView(Wrapper<QuxiaokechengEntity> wrapper);
   	
   	QuxiaokechengView selectView(@Param("ew") Wrapper<QuxiaokechengEntity> wrapper);
   	
   	PageUtils queryPage(Map<String, Object> params,Wrapper<QuxiaokechengEntity> wrapper);
   	

}

