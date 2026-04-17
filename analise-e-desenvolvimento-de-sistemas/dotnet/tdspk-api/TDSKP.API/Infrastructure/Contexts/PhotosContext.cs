using Microsoft.EntityFrameworkCore;
using TDSKP.API.Infrastructure.Mappings;
using TDSPK.API.Infrastructure.Persistence;

namespace TDSPK.API.Infrastructure.Contexts
{
    public class PhotosContext(DbContextOptions<PhotosContext> options) : DbContext(options)
    {
        public DbSet<Photo> Photos { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.ApplyConfiguration(new PhotoMapping());
        }
        public DbSet<TDSKP.API.Infrastructure.Persistence.User> User { get; set; } = default!;

        //EFCore.NamingConventions
        //protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        //{
        //    optionsBuilder.UseSnakeCaseNamingConvention();
        //}
    }
}
