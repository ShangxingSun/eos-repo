#include <eosiolib/eosio.hpp>
#include <eosiolib/asset.hpp>
#include <eosiolib/contract.hpp>
#include <eosiolib/crypto.h>
#include <eosiolib/transaction.hpp>

using namespace eosio;
class getnumber : public contract {
	private:
		uint64_t seed = 0;
	public:
		using contract::contract;

		[[eosio::action]]
			void hi ( name user ) {
				seed = current_time();

				capi_checksum256 result;
				sha256((char *)&seed, sizeof(seed), &result);
				seed = result.hash[1];
				seed <<= 32;
				seed |= result.hash[0];
				printf("%d", (uint32_t)(seed % 100));



			}
};
EOSIO_DISPATCH( getnumber, (hi))
