package com.weljak.storageservice.message.newsrepo;

import com.weljak.storageservice.message.Tags;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TagsRepo extends JpaRepository<Tags, String> {
}
