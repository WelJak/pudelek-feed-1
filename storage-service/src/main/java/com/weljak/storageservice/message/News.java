package com.weljak.storageservice.message;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.util.List;
import java.util.Set;

@Entity
@Getter
@Setter
@NoArgsConstructor
public class News {

    @Id
    @Column(name = "uuid", unique = true, nullable = false, updatable = false)
    private String uuid;

    @Column(name = "type", nullable = false)
    private String type;

    @Column(name = "entryid", nullable = false)
    private String entryid;

    @Column(name = "post_date", nullable = false)
    private String post_date;

    @Column(name = "title", nullable = false)
    private String title;

    @Column(name = "description", nullable = false)
    private String description;

    @OneToMany(mappedBy = "uuid")
    private Set<Tags> tags;

    @Column(name ="link", nullable = false)
    private String link;
}
