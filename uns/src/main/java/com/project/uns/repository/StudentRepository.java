package com.project.uns.repository;
import org.springframework.data.jpa.repository.JpaRepository;
import com.project.uns.model.Student;


public interface StudentRepository extends JpaRepository<Student, Long>{

    boolean existsByJmbg(String jmbg);
    
}
