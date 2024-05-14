package com.dao;

import com.entity.JiaolianfenpeiEntity;
import com.baomidou.mybatisplus.mapper.BaseMapper;
import java.util.List;
import java.util.Map;
import com.baomidou.mybatisplus.mapper.Wrapper;
import com.baomidou.mybatisplus.plugins.pagination.Pagination;

import org.apache.ibatis.annotations.Param;
import com.entity.vo.JiaolianfenpeiVO;
import com.entity.view.JiaolianfenpeiView;


/**
 * 教练分配
 * 
 * @author 
 * @email 
 * @date 2022-04-20 00:17:36
 */
public interface JiaolianfenpeiDao extends BaseMapper<JiaolianfenpeiEntity> {
	
	List<JiaolianfenpeiVO> selectListVO(@Param("ew") Wrapper<JiaolianfenpeiEntity> wrapper);
	
	JiaolianfenpeiVO selectVO(@Param("ew") Wrapper<JiaolianfenpeiEntity> wrapper);
	
	List<JiaolianfenpeiView> selectListView(@Param("ew") Wrapper<JiaolianfenpeiEntity> wrapper);

	List<JiaolianfenpeiView> selectListView(Pagination page,@Param("ew") Wrapper<JiaolianfenpeiEntity> wrapper);
	
	JiaolianfenpeiView selectView(@Param("ew") Wrapper<JiaolianfenpeiEntity> wrapper);
	

}
