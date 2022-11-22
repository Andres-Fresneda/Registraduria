package ProjectCiclo4A.BK_seguridad.repositorios;

import ProjectCiclo4A.BK_seguridad.modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioPermiso  extends MongoRepository<Permiso, String> {
    @Query("{'url':?0,'metodo':?1}")
    Permiso getPermiso(String url, String metodo);
}


