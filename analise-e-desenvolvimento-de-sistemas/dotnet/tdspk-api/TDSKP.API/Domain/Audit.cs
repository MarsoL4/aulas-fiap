using TDSKP.API.Domain.Enums;

namespace TDSKP.API.Domain
{
    public class Audit
    {
        public DateTime DateCreated { get; set; }
        public DateTime DateModified { get; set; }
        public StatusType Status { get; protected set; }

    }
}
