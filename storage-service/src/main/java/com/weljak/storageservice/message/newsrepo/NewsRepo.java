package com.weljak.storageservice.message.newsrepo;

import com.weljak.storageservice.message.News;
import org.springframework.data.jpa.repository.JpaRepository;

public interface NewsRepo extends JpaRepository<News, String> {
    News findByUuid(String uuid);
}
