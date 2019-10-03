package com.weljak.storageservice.message;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.util.List;

@Entity
@Getter
@Setter
@NoArgsConstructor
public class Tags {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "uuid", unique = true, nullable = false, updatable = false)
    private String uuid;

    @ManyToOne
    @Column(name = "tags", nullable = false)
    private News tags;

}
