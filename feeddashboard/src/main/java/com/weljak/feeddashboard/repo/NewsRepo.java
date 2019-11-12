package com.weljak.feeddashboard.repo;

import com.weljak.feeddashboard.domain.News;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface NewsRepo extends JpaRepository<News, String> {

}
