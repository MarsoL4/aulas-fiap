using TDSKP.API.Domain;
using TDSKP.API.Domain.Enums;
using TDSPK.API.Infrastructure.Persistence;

namespace TDSKP.API.Infrastructure.Persistence
{
    public class User : Audit
    {
        public Guid Id { get; private set; }
        public string Name { get; private set; }

        //Um usuário pode ter várias fotos (e uma foto pertence a um único Usuário):
        private readonly List<Photo> _photos = new();
        public IReadOnlyCollection<Photo> Photos => _photos.AsReadOnly();

        public User(string name)
        {
            Id = Guid.NewGuid();
            
            Name = name ?? throw new Exception("Nome não pode ser vazio"); ; //?? -> Verifica se é nulo

            Status = StatusType.Active;
        }

        public void AddPhoto(string url)
        {
            var photo = Photo.Create(url, Id);

            _photos.Add(photo);
        }
    }
}
